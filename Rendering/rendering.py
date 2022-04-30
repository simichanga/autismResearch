import trimesh
import pyrender

fuze_trimesh = trimesh.load("Crate1/Crate1.obj")
mesh = pyrender.Mesh.from_trimesh(fuze_trimesh)
scene = pyrender.Scene()
scene.add(mesh)

pyrender.Viewer(scene, use_raymond_lighting=True)
