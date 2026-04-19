# Copyright TU Wien (2022) - EVC: Task3
# Computer Vision Lab
# Institute of Computer Graphics and Algorithms

import numpy as np
import scipy.ndimage


def evc_demosaic_pattern(
    input_image: np.ndarray, pattern: str = "RGGB"
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Extracts the red, green and blue values of the 'input' image. Results are
    stored in the R, G, B variables.

    Args:
        input_image: Bayer-Pattern image.
        pattern: Bayer-Pattern.

    Returns:
        A tuple (R, G, B), where
          - R is the red channel of the image. (without interpolation)
          - B is the green channel of the image. (without interpolation)
          - G is the blue channel of the image. (without interpolation)
    """
    ### STUDENT CODE
    # TODO: Implement this function.
    # HINT: For this task the "start:end:step" array slicing might be useful.
    #       Find the correct Bayer-Pattern depending on your dataset.
    #       No interpolation needs to be performed here!

    # NOTE: The following three lines can be removed. They prevent the framework
    #       from crashing.

    R = np.zeros(input_image.shape)
    G = np.zeros(input_image.shape)
    B = np.zeros(input_image.shape)
    ### END STUDENT CODE

    return R, G, B


def evc_transform_neutral(
    R: np.ndarray,
    G: np.ndarray,
    B: np.ndarray,
    asShotNeutral: tuple[float, float, float],
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Changes the red, green and blue channels depending on the neutral white
    value (asShotNeutral). Therefore, every channel needs to be divided by the
    respective channel of the white value.

    Args:
        R: The red channel of the image.
        G: The green channel of the image.
        B: The blue channel of the image.
        asShotNeutral: The neutral white value. (RGB vector)

    Returns:
        A tuple (R_trans, G_trans, B_trans), where
          - R_trans is the red channel of the image. (changed by neutral white
            value)
          - G_trans is the green channel of the image. (changed by neutral white
            value)
          - B_trans is the blue channel of the image. (changed by neutral white
            value)
    """
    ### STUDENT CODE
    # TODO: Implement this function.
    # NOTE: The following three lines can be removed. They prevent the framework
    #       from crashing.

    R_trans = np.zeros(R.shape)
    G_trans = np.zeros(G.shape)
    B_trans = np.zeros(B.shape)
    ### END STUDENT CODE

    return R_trans, G_trans, B_trans


def evc_interpolate(
    red: np.ndarray, green: np.ndarray, blue: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Interpolates the red, green and blue channels. In the final image, every
    pixel now has red, green and blue values.

    Args:
        red: The red channel of the image.
        green: The green channel of the image.
        blue: The blue channel of the image.

    Returns:
        A tuple (R_inter, G_inter, B_inter) where
          - R_inter is the red channel of the image (without missing values)
          - G_inter is the green channel of the image (without missing values)
          - B_inter is the blue channel of the image (without missing values)
    """
    ### STUDENT CODE
    # TODO: Implement this function.
    # HINT: The function 'scipy.ndimage.correlate' might be useful.

    # NOTE: The following three lines can be removed. They prevent the framework
    #       from crashing.

    R_inter = np.zeros(np.shape(red))
    G_inter = np.zeros(np.shape(green))
    B_inter = np.zeros(np.shape(blue))

    ### END STUDENT CODE

    return R_inter, G_inter, B_inter


def evc_concat(R: np.ndarray, G: np.ndarray, B: np.ndarray) -> np.ndarray:
    """
    Combines the three individual red, green and blue channels to a single
    image.

    Args:
        R: The red channel of the image.
        G: The green channel of the image.
        B: The blue channel of the image.

    Returns:
        The resulting image.
    """
    ### STUDENT CODE
    # TODO: Implement this function.
    # HINT: The function 'np.stack' might be useful.

    # NOTE: The following line can be removed. It prevents the framework
    #       from crashing.

    result = np.zeros([*R.shape[:2], 3])

    ### END STUDENT CODE

    return result
