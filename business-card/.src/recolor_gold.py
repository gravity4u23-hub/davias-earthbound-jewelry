import numpy as np
from PIL import Image
import pathlib
src = pathlib.Path.home()/"workspace/goals/jamiry-healing-bead-jewelry/files/davias-business-card/.src/media/davias-logo.jpg"
out = pathlib.Path.home()/"workspace/goals/jamiry-healing-bead-jewelry/files/davias-business-card/.src/media/davias-logo-gold-letters.jpg"
im = Image.open(src).convert("RGB")
arr = np.asarray(im).astype(np.float32)/255.0
hsv = np.asarray(im.convert("HSV")).astype(np.float32)
H = hsv[:,:,0]*360.0/255.0
S = hsv[:,:,1]/255.0
V = hsv[:,:,2]/255.0
h_img, w_img = H.shape
Y = np.arange(h_img)[:,None].repeat(w_img, axis=1)
y_start = 1065
# hue in purple-blue-pink range
hue_dist = np.where((H>=185)&(H<=335), 1.0, 0.0)
# strength based on saturation and value, feathered
sat_strength = np.clip((S-0.10)/0.18, 0, 1)
val_strength = np.clip((V-0.42)/0.20, 0, 1)
row_strength = np.clip((Y - (y_start-8))/16.0, 0, 1)
mask = hue_dist * sat_strength * val_strength * row_strength
# also pale near-white letter cores: low sat, very bright, hue in range, below y_start
core = ((S<0.28)&(V>0.82)&(H>=170)&(H<=335)).astype(np.float32) * row_strength * np.clip((V-0.82)/0.10,0,1)
# transformed version: set hue to gold, boost saturation for coloured pixels, pale gold for cores
# Build transformed HSV
H2 = np.full_like(H, 43.0)
S2 = np.clip(S*1.55+0.12, 0, 1)
V2 = V
# for core pixels, pale gold saturation
S2 = np.where(core>mask, 0.48, S2)
alpha = np.maximum(mask, core*0.85)
# Convert transformed HSV back to RGB vectorised
# Use PIL for conversion of full transformed image
hsv2 = np.stack([ (H2*255/360).astype(np.uint8), (S2*255).astype(np.uint8), (V2*255).astype(np.uint8)], axis=2)
gold_rgb = np.asarray(Image.fromarray(hsv2, mode="HSV").convert("RGB")).astype(np.float32)/255.0
a = alpha[:,:,None]
blended = arr*(1-a) + gold_rgb*a
Image.fromarray((np.clip(blended,0,1)*255).astype(np.uint8)).save(out, quality=94)
print("saved", out, "mask px", int((alpha>0.5).sum()))
