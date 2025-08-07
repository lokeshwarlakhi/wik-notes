from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, TextArea
from .__version__ import __version__
class NoteTaker(App):
    """AI-powered note-taking TUI."""

    BINDINGS = [("ctrl+q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield TextArea(id="notepad")
        yield Footer()

    def on_mount(self) -> None:
        self.title = f"AI Note Taker v{__version__}"  # From __version__.py

def main():
    app = NoteTaker()
    app.run()

if __name__ == "__main__":
    main()