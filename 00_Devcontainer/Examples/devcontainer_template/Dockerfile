FROM python:3.11-slim

# Create a non-root user
RUN useradd -m -u 1000 -s /bin/bash vscode

WORKDIR /workspace

# Change ownership of the workspace
RUN chown -R vscode:vscode /workspace

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=vscode:vscode . .

# Switch to non-root user
USER vscode

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]