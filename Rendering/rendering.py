import trimesh
import pyrender
import numpy as np

tm = trimesh.load('MaleLow.obj')
m = pyrender.Mesh.from_trimesh(tm)
m.primitives

scene = pyrender.Scene()
scene.add(m)

pyrender.Viewer(scene, use_raymond_lighting = True)
