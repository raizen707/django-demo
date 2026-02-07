import json
from django.http import StreamingHttpResponse
from django.shortcuts import render
import time

# Create your views here.
def stream_json(request):
    def generate():
        for i in range(5):
            data = {
                "number": i,
                "message": f"Hello {i}"
            }
            yield json.dumps(data) + "\n"

    return StreamingHttpResponse(
        generate(),
        content_type="application/x-ndjson"
    )

def json_stream(request):
    return StreamingHttpResponse(generate(), content_type="application/x-ndjson")

def generate():
    for i in range(5):
        yield json.dumps({"step": i}) + "\n"
        time.sleep(1)

def stream_page(request):
    return render(request, "stream.html")

def json_page(request):
    return render(request, "stream.html")