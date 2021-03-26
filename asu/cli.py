from typing import List
import typer
import sys
import asu.s3 as s3

app = typer.Typer()

@app.command()
def lsenc():
    s3.describe_all_buckets_encryption()

def main(args: List[str] = sys.argv[1:]) -> None:
    app(args)

if __name__ == "__main__":
    main()
