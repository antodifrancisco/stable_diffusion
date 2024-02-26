import torch
from torch import nn
from torch.nn import functional as F
import math


class SelfAttention(nn.Module):

    def __init__(self, n_heads: int, d_embed: int, in_proj_bias=True, out_proj_bias=True) -> None:
        super().__init__()

        self.in_proj = nn.Linear(d_embed, 3 * d_embed, bias=in_proj_bias)
        self.out_proj = nn.Linear(d_embed, d_embed)
