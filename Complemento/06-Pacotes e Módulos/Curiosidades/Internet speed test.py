import speedtest

st = speedtest.Speedtest()

print(f"Download speed: {st.download()}")
print(f"Upload speed: {st.upload()}")