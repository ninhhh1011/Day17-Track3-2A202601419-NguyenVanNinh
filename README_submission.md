# Báo Cáo Nộp Bài — Lab 17: Multi-Memory Agent với Zep

**Học viên:** Nguyễn Văn Ninh  
**Mã SV:** 2A202601419  
**Bài Lab:** Lab 17 — Multi-Memory Agent Systems with Zep Cloud V3  

---

## 1. Ba Câu Hỏi Cốt Lõi Về Kiến Trúc Bộ Nhớ

### Câu 1: Layer quan trọng nhất trong bộ test này & Case minh chứng
Trong bộ test này, **Long-Term Memory (Zep User Graph Context Block)** và **Episodic Memory** đóng vai trò quyết định nhất:
- **Long-Term Memory** quyết định 4/11 cases (`E02`, `E03`, `E08`, `E09`). Nó duy trì preferences (`E02` thích Python), open-loop TODOs (`E03` deadline 16:00), đảm bảo phân lập dữ liệu người dùng (`E09` Lan không lộ project của Minh), và tự động cập nhật xung đột thời gian (`E08` ưu tiên TypeScript cho BLUEBIRD-42).
- **Episodic Memory** (`E04`, `E05`) là tầng duy nhất truy hồi được lộ trình hành động (trajectory) và bài học thực tế từ sự cố quá khứ (fix async timeout bằng `ClientSession` và nguyên nhân `connection churn`).

### Câu 2: Trade-off giữa Zep Context Block và Tự Xây Dựng Redis + Qdrant
- **Managed Zep V3 Context Block**: Tự động trích xuất entities, xây dựng đồ thị quan hệ hai chiều, tự tính toán điểm relevance và giải quyết xung đột thời gian (temporal recency). Tiết kiệm chi phí token do context được tổng hợp sẵn, nhưng phụ thuộc vào cloud latency và hạn chế kiểm soát thuật toán chunking/ranking nội bộ.
- **Tự dựng Redis + Qdrant (Local Baseline)**: Cho phép toàn quyền tùy biến embedding model, tốc độ truy xuất cực nhanh (sub-millisecond), bảo mật dữ liệu tuyệt đối (on-premise). Tuy nhiên, đòi hỏi phải tự viết logic phức tạp để đồng bộ state, de-duplicate facts, quản lý đồ thị quan hệ và dễ bị "context dilution" do vector search thuần túy thiếu hiểu biết về graph relations.

### Câu 3: Guardrail Chống Memory Poisoning (Đầu Độc Bộ Nhớ)
Để ngăn chặn user tiêm prompt injection độc hại vào bộ nhớ bền vững (durable memory):
1. **Validation & Sanitization Gate**: Sử dụng `privacy_guard.py` và LLM Judge để kiểm duyệt mọi message trước khi đưa vào durable ingestion (chỉ chấp nhận facts/constraints khách quan, từ chối prompt đổi vai trò/ghi đè system instruction).
2. **Provenance & Source Attribution**: Mọi episode/fact phải gắn kèm metadata nguồn (`thread_id`, `timestamp`, `session_stage`). Khi có mâu thuẫn, chỉ cấp quyền ghi đè cho các kênh/vai trò có thẩm quyền (Human-in-the-loop validation).

---

## 2. Bốn Câu Phân Tích Benchmark

1. **Layer có hit rate thấp nhất**: Trong baseline `no_memory`, Long-Term và Episodic có hit rate **0%** do không thể nhớ qua các session. Trong student run, cả 4 layer đều đạt **100% hit rate** nhờ định tuyến chính xác và token budget hợp lý.
2. **Query retrieve nhiều token nhất**: Query `E07` (Mixed layer) và `E10` (Compaction fixture) tiêu tốn nhiều token nhất do cần tổng hợp đồng thời nhiều nguồn dữ liệu (Long-term preference + Semantic rule hoặc Fixture history).
3. **Case Mixed (E07)**: Cần kết hợp **Long-Term Memory** (xác định user thích ngôn ngữ `Python`) và **Semantic Memory** (quy tắc thanh toán với header `Idempotency-Key`). Evidence bắt buộc phải chứa cả hai yếu tố này.
4. **Token Reduction vs Hit Rate**: `no_memory` có token reduction cao (không retrieve gì) nhưng hit rate cực thấp (chỉ pass E01). Giảm token chỉ có ý nghĩa khi **giữ lại đúng evidence cốt lõi**; việc cắt tỉa quá đà sẽ làm mất các marker quyết định (như literal codes).

---

## 3. Phân Tích Cơ Chế Đặc Thù (E08 Recency & E10 Compaction)

- **E08 (Recency / Conflict Resolution)**: Khi Minh chuyển từ dự án cũ (Python) sang dự án mới `BLUEBIRD-42` (TypeScript/NestJS), Zep Graph gán `validity_range` mới cho quan hệ hiện tại. Khi query cho dự án mới, Context Block trả về `TypeScript` là preference hiện hành, bảo toàn lịch sử mà không bị lẫn lộn dữ liệu cũ.
- **E10 (Short-Term Compaction)**: Cơ chế Sliding Window (giữ 4–6 tin nhắn gần nhất) khi kích hoạt áp lực token sẽ nén các turn đàm thoại cũ thành tóm tắt có cấu trúc. Hàm `extract_durable_notes` tự động phát hiện và bảo tồn nguyên vẹn deadline `REVIEW-DEADLINE-1600` cùng mốc `Friday 16:00` dù các câu nói ban đầu đã bị loại bỏ khỏi buffer.
