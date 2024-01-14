from pydub import AudioSegment
import random
import os
import csv

def change_pitch(audio, factor):
    return audio._spawn(audio.raw_data, overrides={
        "frame_rate": int(audio.frame_rate * factor)
    })

def append_to_csv(csv_file, data):
    with open(csv_file, 'a', newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def generate_pitch_variations(input_file, output_folder, csv_file,message,response, num_variations=200):
    # Cargar el archivo de audio original
    original_audio = AudioSegment.from_wav(input_file)

    # Crear el directorio de salida si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Generar 200 variaciones de tono
    for i in range(num_variations):
        # Seleccionar un factor de cambio de tono aleatorio entre 0.5 y 1.5
        pitch_factor = random.uniform(0.5, 1.5)

        # Modificar el tono del audio original
        modified_audio = change_pitch(original_audio, pitch_factor)

        # Guardar el nuevo archivo de audio
        output_file_name = input_audio_file.removesuffix(".wav")
        output_file_name = output_file_name.removeprefix("audios/")
        output_file = os.path.join(output_folder, f"{output_file_name}{i + 1}.wav")
        output_file_name = f"{output_file_name}{i + 1}.wav"
        modified_audio.export(output_file, format="wav")

        # Agregar una fila al archivo CSV con la información del archivo original y modificado
        append_to_csv(csv_file, [output_file_name,message,response])

if __name__ == "__main__":
    input_audio_file = 'audios/cualnombre.wav'
    output_folder = "audios"
    csv_file = "data.csv"

    generate_pitch_variations(input_audio_file, output_folder, csv_file, "¿CUÁL ES TU NOMBRE?","SOY CHATO UN ASISTENTE VIRTUAL",num_variations=200)
