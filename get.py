import requests
from rich.table import Table
from rich.console import Console


url = "https://jsonplaceholder.typicode.com/posts"


try:
    get_response = requests.get(url, timeout=5)
    get_response.raise_for_status()  # raises exception for 4xx/5xx codes
    post_response = requests.post(url,
    json={"title": "Route 101 Performance Report",
    "body": "On-time percentage: 83.3%",
    "userId": "1"}
)
    post_response.raise_for_status()  # protect the POST too
    data = get_response.json()
    new_record = post_response.json()
    console = Console()
    table = Table(title="Posts")
    table.add_column("User", style ="cyan")
    table.add_column("Title", style ="magenta")
    for post in data[:5]:
     table.add_row(
        str(post['id']),
        str(post['title'])
        
    )
        
    console.print(table)
    print(f"\n✅ Report submitted!")
    print(f"New record ID: {new_record['id']}")
    print(f"Title: {new_record['title']}")
except requests.exceptions.Timeout:
    print("Request timed out.")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
except requests.exceptions.ConnectionError:
    print("No internet connection.")
