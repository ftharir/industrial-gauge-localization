import torch

# بررسی نسخه PyTorch
print(f"PyTorch Version: {torch.__version__}")

# بررسی اینکه آیا CUDA (GPU) در دسترس است
print(f"Is CUDA available? {torch.cuda.is_available()}")
