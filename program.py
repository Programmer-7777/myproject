import eng_to_ipa as ipa
transcription = ipa.convert("The quick brown fox jumped over the lazy dog")
print("[", end="")
print(transcription, end="")
print("]")