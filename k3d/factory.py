class Factory:
    @classmethod
    def torus_knot(cls, view_matrix):
        return {
            'type': 'TorusKnot',
            'modelViewMatrix': cls.__matrix_to_list(view_matrix),
            'color': 0xff00ff,
            'knotsNumber': 16,
            'radius': 7,
            'tube': 2
        }

    @classmethod
    def text(cls, view_matrix, string, color = 0xFFFFFF, font_weight = 'bold', font_face = 'Courier New'):
        return {
            'type': 'Text',
            'modelViewMatrix': cls.__matrix_to_list(view_matrix),
            'text': string,
            'color': color,
            'fontOptions': {
                'face': font_face,
                'weight': font_weight
            }
        }

    @classmethod
    def points(cls, view_matrix, positions, colors, point_size = 1.0):
        return {
            'type': 'Points',
            'modelViewMatrix': cls.__matrix_to_list(view_matrix),
            'pointSize': point_size,
            'pointsPositions': cls.__matrix_to_list(positions),
            'pointsColors': cls.__matrix_to_list(colors),
        }

    @staticmethod
    def __matrix_to_list(matrix):
        return list(sum(matrix, ()))