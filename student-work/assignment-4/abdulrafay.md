# Abdul Rafay

Hi all, my name is Abdul Rafay. I am a senior majoring in Data Science.

My favorite programming language is, Python. It is the one I worked most with on various projects; ML, NLP, and so on.

## Example Code

```
# 6. 디코딩 함수
def decode_sequence(input_seq):
    states_value = encoder_model.predict(input_seq)

    target_seq = np.zeros((1, 1, num_decoder_tokens))
    decoded_sentence = ""

    for _ in range(max_decoder_seq_length):
        output_tokens, h, c = decoder_model.predict([target_seq] + states_value)

        sampled_token_index = np.argmax(output_tokens[0, -1, :])
        sampled_char = reverse_target_index[sampled_token_index]
        decoded_sentence += sampled_char

        if len(decoded_sentence) > max_decoder_seq_length:
            break

        target_seq = np.zeros((1, 1, num_decoder_tokens))
        target_seq[0, 0, sampled_token_index] = 1.0
        states_value = [h, c]

    return decoded_sentence
```

### Code Explanation

The code above is a tiny snippet from an NLP project. Our goal was to create a deobfuscator for very specific type of encoding in Korean text. The code above is a function that helps overall model to decode a sequence.
