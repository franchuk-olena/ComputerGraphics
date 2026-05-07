from src.engine.model.Model import Model
from src.engine.model.SimplePolygon import SimplePolygon
from src.engine.scene.Scene import Scene


class Tetrahedron(Model):

    def __init__(self,
                 alpha=1.0,
                 color="cyan",
                 edge_color="blue",
                 line_style="-",
                 line_width=1.0,
                 ):
        super().__init__()
        self.polygons = []

        vertices = [
            [0, 0, 0],  # A
            [1, 0, 0],  # B
            [0, 1, 0],  # C
            [0, 0, 1],  # D
        ]

        faces = [
            [vertices[j] for j in [0, 1, 2]],  # ABC
            [vertices[j] for j in [0, 1, 3]],  # ABD
            [vertices[j] for j in [0, 2, 3]],  # ACD
            [vertices[j] for j in [1, 2, 3]],  # BCD
        ]

        for face in faces:
            self.polygons.append(
                SimplePolygon(
                    *face,
                    color=color,
                    edgecolor=edge_color,
                    alpha=alpha,
                    line_width=line_width,
                    line_style=line_style,
                )
            )

    def draw_model(self, plt_axis):
        for polygon in self.polygons:
            polygon.transformation = self.transformation
            polygon.pivot(self._pivot)
            polygon.draw(plt_axis)

    def apply_transformation_to_geometry(self):
        super().apply_transformation_to_geometry()

        for polygon in self.polygons:
            polygon.apply_transformation_to_geometry()


if __name__ == '__main__':
    TETRA_KEY = "tetra"

    tetra = Tetrahedron(alpha=0.3, color="orange")
    tetra.show_pivot()
    tetra.show_local_frame()

    scene = Scene()
    scene[TETRA_KEY] = tetra
    scene.show()