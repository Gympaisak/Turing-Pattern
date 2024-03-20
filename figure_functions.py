import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def show_patterns(U):
    """Shows pattern for one of the morphogens,
        with colorspectrum YlOrBr """
    fig, ax = plt.subplots(1, 1, figsize=(4, 4))
    ax.imshow(U, cmap=plt.cm.YlOrBr,    # colormap from white to dark brown
              interpolation='bilinear',
              extent=[-1, 1, -1, 1])
    ax.set_axis_off()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def numpy2pil_help(np_array: np.ndarray) -> Image:
    """
    Convert an HxWx3 numpy array into an RGB Image
    """

    assert_msg = 'Input shall be a HxWx3 ndarray'
    assert isinstance(np_array, np.ndarray), assert_msg
    assert len(np_array.shape) == 3, assert_msg
    assert np_array.shape[2] == 3, assert_msg

    img = Image.fromarray(np_array, 'RGB')
    return img

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def numpy2pil(U, V, rows, columns, save=False, res=False):
    """
    Creates 500x500 image of U and V morphogens
    """
    pU = np.zeros((rows, columns), dtype=np.uint8)
    pV = np.zeros((rows, columns), dtype=np.uint8)

    maxU = np.max(U)
    maxV = np.max(V)

    for r in range(rows):
        for c in range(columns):
            pU[r, c] = int(U[r, c] / maxU*255)
            pV[r, c] = int(V[r, c] / maxV*255)

    Z = np.zeros((rows, columns), dtype=np.uint8)

    result = np.stack((Z, pU, pV), axis=2, dtype=np.uint8)
    img = numpy2pil_help(result)
    #img.save('output.png')
    #img.show()
    img = img.resize((500, 500))
    if save is True:
        img.save('myimage_500.jpg')
    
    if res is True:
        return result
    else:
        return img