import tensorflow as tf

graph_def_file = "tf_files/retrained_graph.pb"
input_arrays = ["model_inputs"]
output_arrays = ["model_outputs"]

converter = tf.lite.TFLiteConverter.from_frozen_graph(
        graph_def_file, input_arrays, output_arrays)
tflite_model = converter.convert()
open("tf_files/converted_model.tflite", "wb").write(tflite_model)