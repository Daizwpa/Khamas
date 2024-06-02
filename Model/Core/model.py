import tensorflow as tf


def augmentationLayer(x):
    data_augmentation = tf.keras.Sequential([
        tf.keras.layers.RandomFlip('horizontal'),
        tf.keras.layers.RandomRotation(0.2),
    ])
    return data_augmentation(x)


def pre_processLayer(x):
    preprocess_input = tf.keras.applications.resnet50.preprocess_input
    return preprocess_input(x)


def base_modelLayer(x, shape, batch, weights='imagenet'):
    base_model = tf.keras.applications.ResNet50(input_shape=shape,
                                                include_top=False,
                                                weights=weights)
    base_model.trainable = False
    return base_model(x)


def make_model(batch, shape):
    model = None
    try:
        input = tf.keras.Input(shape=shape)
        x = augmentationLayer(input)
        x = pre_processLayer(x)
        x = base_modelLayer(x, shape=shape, batch=batch)
        x = tf.keras.layers.GlobalAveragePooling2D()(x)
        x = tf.keras.layers.Dropout(0.2)(x)
        output = tf.keras.layers.Dense(1, activation='sigmoid')(x)
        model = tf.keras.Model(input, output)
    except:
        raise
    return model
