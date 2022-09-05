import sys, os
import torch
import torch.nn.functional as F

sys.path.insert(0,"taming_transformers")
import taming



class Transformer(torch.nn.Module):
    
    def __init__(self, weights, resolution=256):
        super().__init__()
        
        if weights == "imagenet":
            weights = "weights/2021-04-03T19-39-50_cin_transformer.pth"
        elif weights == "celeba":
            weights = "weights/2020-11-13T21-41-45_faceshq_transformer.pth"
        
        self.model = torch.load(weights)
        
        self.upsample = torch.nn.Upsample(size=(resolution, resolution), mode='bilinear', align_corners=False)
    
    def encode(self, x):
        x = (x*2 - 1.0)
        x = self.upsample(x)
        return self.model.encode(x)[0]
    
    def decode(self, z, image_shape=None):
        xp = self.model.decode(z)
        xp = (xp+1)/2
        xp = torch.clip(xp, 0,1)
        return xp
    
    def forward(self, x):
        return self.decode(self.encode(x))
