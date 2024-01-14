clear a;
%Ajustes arduino
a = arduino('COM3', 'Uno');
ledPin = 'D13';
%Diccionario morse
morseCodeMap = containers.Map(...
    {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', ...
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ...
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' '}, ...
    {'.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', ...
    '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', ...
    '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----', '/'});

message = 'HOLA';
write_morse(message,morseCodeMap,a,ledPin);

function write_morse(message,morseCodeMap,a,ledPin)
    for i = 1:length(message)
        character = upper(message(i));
        if isKey(morseCodeMap, character)
            morse = morseCodeMap(character);
            for j=1:length(morse)
                a.writeDigitalPin(ledPin,1);
                if morse(j) == '-'
                    pause(0.34);
                else
                    pause(0.12);
                end
                a.writeDigitalPin(ledPin,0);
                pause(0.1);
            end
           fprintf("%s",morseCodeMap(character));
        end
    end
end