import trimesh
import pyrender

fuze_trimesh = trimesh.load("Crate1/Crate1.obj")
mesh = pyrender.Mesh.from_trimesh(fuze_trimesh)
# mesh = trimesh.load_mesh('humanModel/humanModel.obj', process=False)
scene = pyrender.Scene()
scene.add(mesh)

pyrender.Viewer(scene, use_raymond_lighting=True)
