from huggingface_hub import snapshot_download
model_id="teknium/OpenHermes-2.5-Mistral-7B"
snapshot_download(repo_id=model_id, revision="main")


