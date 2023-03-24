from replacetext import text_replace
import speech_recognition as speech_reco
saved_text_file = "./saved.txt"
energy_threshold = 1000
sampling_rate = 44100
sizeof_chunk = 1024


def convert_SpeechToText():
    # Using the try catch block we are checking if the file "saved.txt " exists or not. If the file exists, we will append
    # to the existing file, if it does not exist, we will write to the file.
    try:
        text_file = open(saved_text_file, "a+", encoding="utf-8")
    except FileNotFoundError:
        text_file = open(saved_text_file, "w+", encoding="utf-8")
    # We will now create an instance of the recognizer from the SpeechRecognition library
    r = speech_reco.Recognizer()
    # Setting the energy threshold value for the created instance of the recognizer to our pre defined value
    r.energy_threshold = energy_threshold
    with speech_reco.Microphone(sample_rate=sampling_rate, chunk_size=sizeof_chunk) as source:
        # Listening for 1 second to calibrate the energy threshold. This will adjust the value according to
        # the surrounding noise levels
        print("Please wait. Calibrating microphone...This will take just one second")
        # This duration can be changed according to the requirement.
        r.adjust_for_ambient_noise(source, duration=1)
        print('You can speak something now')
        voice_produced = r.listen(source)
        try:
            # We will use Google Speech API to identify the speech and convert it to text
            generated_text = r.recognize_google(
                voice_produced, language="en-IN")
            # This will replace our generated text with list of symbols that we have created if there is a match.
            # This helps in producing a more accurate and logical result
            generated_text = text_replace(generated_text)
            # Printing out the speech to text conversion
            print('You said the following : {} '.format(generated_text))
            # Writing the text to our file in order to keep  a track of the previous conversations
            text_file.write(generated_text+'\n')
            # Closing the text file
            text_file.close()
            # Returning the generated text
            return generated_text
        except:
            print("Could not recognize what you just said. Please try again.")
            # In this case we will return nothing
            return None
