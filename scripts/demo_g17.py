from __future__ import annotations

import json
import sys

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from src.config import settings
from src.memory_student import StudentMemory
from src.zep_common import get_zep_client

console = Console(highlight=False)


def demo_case_g17() -> None:
    console.print(
        Panel.fit(
            "[bold yellow]VIET HERITAGE AI - DEMO TEST CASE G17 (MIXED MEMORY LAYER)[/bold yellow]\n"
            "[italic cyan]Ket hop Long-Term Memory (Company Stack) & Semantic Memory (Payment Policy)[/italic cyan]",
            border_style="bright_yellow",
        )
    )

    with open("data/golden_eval.json", "r", encoding="utf-8") as f:
        golden = json.load(f)["evaluations"]

    g17 = next(c for c in golden if c["id"] == "G17")

    console.print("\n[bold yellow]1. Boi canh & Cau hoi truy van (Query):[/bold yellow]")
    console.print(f"[white]{g17['query']}[/white]\n")

    console.print("[bold yellow]2. Yeu cau Evidence (Ground Truth):[/bold yellow]")
    console.print(f"  • Bat buoc chua: [bold green]{g17['must_contain_all']}[/bold green]")
    console.print(f"  • Cam ro ri: [bold red]{g17.get('must_not_contain', [])}[/bold red] (User Isolation)\n")

    client = get_zep_client()
    memory = StudentMemory(client)

    with console.status("[bold green]Dang truy xuat tu Zep User Graph & Standalone Knowledge Graph...[/bold green]"):
        lt = memory.retrieve_long_term(g17["user_id"], g17["thread_id"], g17["query"])
        sem = memory.retrieve_semantic(settings.semantic_graph_id, g17["query"])
        layers = {"short_term": "", "long_term": lt, "episodic": "", "semantic": sem}
        context, breakdown = memory.assemble_context(layers)

    console.print("[bold yellow]3. Token Budget Breakdown (10/4/3/3 Rule):[/bold yellow]")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Memory Layer")
    table.add_column("Used Tokens", justify="right")
    table.add_column("Limit Tokens", justify="right")
    table.add_column("Status", justify="center")

    for layer, stats in breakdown.items():
        status = "[green]OK[/green]" if stats["used_tokens"] <= stats["limit_tokens"] else "[red]OVER[/red]"
        table.add_row(layer, str(stats["used_tokens"]), str(stats["limit_tokens"]), status)
    console.print(table)

    console.print("\n[bold yellow]4. Noi dung Assembled Context:[/bold yellow]")
    console.print(Panel(context, border_style="cyan", title="Context Injection"))

    console.print("\n[bold yellow]5. Ket qua Kiem tra Khop Evidence:[/bold yellow]")
    all_passed = True
    for marker in g17["must_contain_all"]:
        has_marker = marker in context
        status = "[bold green]PASS[/bold green]" if has_marker else "[bold red]MISSING[/bold red]"
        console.print(f"  • Tim thay '{marker}': {status}")
        if not has_marker:
            all_passed = False

    for forbidden in g17.get("must_not_contain", []):
        is_absent = forbidden not in context
        status = "[bold green]SAFE (No Leak)[/bold green]" if is_absent else "[bold red]LEAKED[/bold red]"
        console.print(f"  • Khong chua '{forbidden}': {status}")
        if not is_absent:
            all_passed = False

    if all_passed:
        console.print(Panel.fit("[bold green]KET QUA G17: PASS HOAN TOAN (100% SUCCESS)![/bold green]", border_style="green"))
    else:
        console.print(Panel.fit("[bold red]KET QUA G17: FAILED[/bold red]", border_style="red"))


if __name__ == "__main__":
    demo_case_g17()
