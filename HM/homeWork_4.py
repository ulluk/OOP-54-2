from rich import print
from rich.console import Console
from rich.table import Table
from rich.progress import track
import time


print("[bold cyan]Привет! Это [green]Rich[/green] в действии![/bold cyan]")

table = Table(title="Оценки студентов")

table.add_column("Имя", justify="left", style="cyan", no_wrap=True)
table.add_column("Предмет", style="magenta")
table.add_column("Оценка", justify="right", style="green")

table.add_row("Алексей", "Математика", "5")
table.add_row("Ирина", "Физика", "4")
table.add_row("Максим", "История", "5")

console = Console()
console.print(table)


print("\n[bold yellow]Загрузка:[/bold yellow]")
for _ in track(range(10), description="Обработка..."):
    time.sleep(0.2)


