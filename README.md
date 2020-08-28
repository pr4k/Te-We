## TE-WE (Terminal Webcam)

I was using my linux and suddenly I realised that I have no application for webcam on my system, So I thought of creating one on my own.
So presenting you the **Webcam Terminal**, A terminal client for webcam made solely with Ascii Characters.

You can find the whole unedited video of programming at :
[youtube.com/how-i-created-a webcam-terminal-client](https://youtu.be/me2RsizTnU4)

---

### Technology Used

It uses Opencv to stream the webcam and break the video into frames, later we use each frame to create an Ascii image of it with different density characters.
Next part is to give each character color based on the original color of image, for this we will be converting the *RGB* color to *ANSI* color which can be displayed on terminal.

### Demo

![Demo](demo.gif)

### How to use:

- Install the required library using `pip install -r requirements.txt`
- Run the script using `python main.py`

**Enjoy**

### To-Do

- Create the calculation part in *Julia* or someother language to speed up the calculation
- Improve the overall performance

---
### Feedback

Feel free to leave any issues or contribute.
