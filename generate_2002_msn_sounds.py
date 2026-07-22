import math
import struct
import wave
import os

def create_wave_file(filename, samples, sample_rate=22050):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with wave.open(filename, 'w') as wav_file:
        # nchannels=1 (mono), sampwidth=2 (16-bit), framerate=sample_rate
        wav_file.setparams((1, 2, sample_rate, len(samples), 'NONE', 'not compressed'))
        packed_samples = bytearray()
        for sample in samples:
            # Clamp sample to 16-bit signed integer range [-32768, 32767]
            val = max(-32768, min(32767, int(sample * 32767.0)))
            packed_samples.extend(struct.pack('<h', val))
        wav_file.writeframes(packed_samples)
    print(f"Generated {filename}")

sample_rate = 22050

# 1. MSN Messenger 4.7 (2002) msnmsg.wav (Incoming Message Chime)
# Dual bell tone (G5 = 783.99 Hz for 0.08s, then C6 = 1046.50 Hz for 0.25s) with soft bell envelope
samples_msg = []
dur1 = int(sample_rate * 0.08)
dur2 = int(sample_rate * 0.25)
total_len = dur1 + dur2

for i in range(dur1):
    t = i / sample_rate
    env = math.exp(-t * 12) * 0.3
    # Fundamental + 2nd harmonic for bell warmth
    val = (math.sin(2 * math.pi * 783.99 * t) + 0.3 * math.sin(2 * math.pi * 1567.98 * t)) * env
    samples_msg.append(val)

for i in range(dur2):
    t = i / sample_rate
    env = math.exp(-t * 8) * 0.35
    val = (math.sin(2 * math.pi * 1046.50 * t) + 0.3 * math.sin(2 * math.pi * 2093.00 * t)) * env
    samples_msg.append(val)

create_wave_file('sounds/type.wav', samples_msg, sample_rate)

# 2. MSN Messenger 4.7 (2002) online.wav (Contact Sign-in Chime)
# 3-note ascending chime: E5 (659.25Hz), G5 (783.99Hz), C6 (1046.50Hz)
samples_online = []
step_len = int(sample_rate * 0.09)

freqs = [523.25, 659.25, 783.99]
for f in freqs:
    for i in range(step_len):
        t = i / sample_rate
        env = math.exp(-t * 10) * 0.3
        val = (math.sin(2 * math.pi * f * t) + 0.25 * math.sin(2 * math.pi * f * 2 * t)) * env
        samples_online.append(val)

create_wave_file('sounds/online.wav', samples_online, sample_rate)

# 3. Outgoing Message Sent (short pop click sweep)
samples_outgoing = []
dur_out = int(sample_rate * 0.06)
for i in range(dur_out):
    t = i / sample_rate
    freq = 300 + (600 - 300) * (i / dur_out)
    env = math.exp(-t * 25) * 0.25
    val = math.sin(2 * math.pi * freq * t) * env
    samples_outgoing.append(val)

create_wave_file('sounds/outgoing.wav', samples_outgoing, sample_rate)

# 4. New Email / File Notification (2002 Hotmail chime)
samples_email = []
email_freqs = [659.25, 783.99, 1046.50]
for f in email_freqs:
    for i in range(int(sample_rate * 0.1)):
        t = i / sample_rate
        env = math.exp(-t * 8) * 0.28
        val = (math.sin(2 * math.pi * f * t) + 0.2 * math.sin(2 * math.pi * f * 2 * t)) * env
        samples_email.append(val)

create_wave_file('sounds/newemail.wav', samples_email, sample_rate)

# 5. Alert Notification (2002 MSN alert chime)
samples_alert = []
alert_freqs = [1046.50, 1567.98]
for f in alert_freqs:
    for i in range(int(sample_rate * 0.12)):
        t = i / sample_rate
        env = math.exp(-t * 12) * 0.3
        val = math.sin(2 * math.pi * f * t) * env
        samples_alert.append(val)

create_wave_file('sounds/newalert.wav', samples_alert, sample_rate)

# 6. Nudge Vibration Sound
samples_nudge = []
dur_nudge = int(sample_rate * 0.45)
for i in range(dur_nudge):
    t = i / sample_rate
    # Low frequency rumble + sawtooth modulation
    freq = 110 + 40 * math.sin(2 * math.pi * 15 * t)
    env = math.exp(-t * 4) * 0.35
    # Sawtooth approximation
    val = (2.0 * (t * freq - math.floor(t * freq + 0.5))) * env
    samples_nudge.append(val)

create_wave_file('sounds/nudge.wav', samples_nudge, sample_rate)

# 7. Phone Ringing Sound
samples_phone = []
dur_phone = int(sample_rate * 0.6)
for i in range(dur_phone):
    t = i / sample_rate
    env = math.sin(2 * math.pi * 2 * t) if (t % 0.3 < 0.2) else 0
    val = (math.sin(2 * math.pi * 440 * t) + math.sin(2 * math.pi * 480 * t)) * 0.15 * env
    samples_phone.append(val)

create_wave_file('sounds/phone.wav', samples_phone, sample_rate)

print("All 2002 MSN Messenger 4.7 WAV audio files generated successfully!")
