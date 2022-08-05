import torch.cuda

def check_for_cuda():
    cuda_available = torch.cuda.is_available()
    if cuda_available:
        return cuda_available, torch.cuda.mem_get_info()
    else:
        return cuda_available, None
