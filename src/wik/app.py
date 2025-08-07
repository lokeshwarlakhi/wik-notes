from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, TextArea,Static
from textual.containers import Container
from .__version__ import __version__


class Sidebar(Container):
    """A sidebar for displaying recent notes or other information."""
    def compose(self) -> ComposeResult:
        yield Static("Sidebar Content 1", classes="sidebar-item")
        yield Static("Sidebar Content 2", classes="sidebar-item")
        yield Static("Sidebar Content 3", classes="sidebar-item") 
class WikNotes(App):
    """AI-powered note-taking TUI."""
    CSS_PATH = "app.css"
    BINDINGS = [
        ("ctrl+b","toggle_sidebar","Toggle Sidebar"),
        ("ctrl+q", "quit", "Quit"),
        ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield TextArea(id="notepad")
        yield Sidebar(id="sidebar" ,classes="-hidden")  # Sidebar is initially hidden
        yield Footer()

    def action_toggle_sidebar(self):
        self.query_one(Sidebar).toggle_class("-hidden")

    def on_mount(self) -> None:
        self.title = f"W.I.K Notes v{__version__}"  # From __version__.py

def main():
    app = WikNotes()
    app.run()

if __name__ == "__main__":
    main()