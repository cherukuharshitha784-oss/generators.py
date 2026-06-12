import typer
from typing_extensions import Annotated

# 1. Initialize the Typer app
app = typer.Typer()


# 2. Explicitly define this function as a command
@app.command()
def greet(
    name: Annotated[
        str,
        typer.Argument(
            help="The (last, if --title is given) name of the person to greet"
        ),
    ] = "",
    title: Annotated[
        str, typer.Option(help="The preferred title of the person to greet")
    ] = "",
    doctor: Annotated[
        bool, typer.Option(help="Whether the person is a doctor (MD or PhD)")
    ] = False,
    count: Annotated[
        int, typer.Option(help="Number of times to greet the person")
    ] = 1,
):
    greeting = "Greetings, "

    if doctor and not title:
        title = "Dr."

    if not name:
        if title:
            # Capitalize it so it looks clean (e.g., "Greetings, Mr!")
            name = title.rstrip(".").capitalize()
            title = ""  # Clear title so we don't repeat it as "Greetings, Mr Mr!"
        else:
            name = "friend"

    if title:
        greeting += f"{title} "

    greeting += f"{name}!"

    for _ in range(count):
        print(greeting)


if __name__ == "__main__":
    app()


