# Helovox

### Read-Me for Helovox Translator Script

The AI Voice Translator is a Python application that leverages several libraries to convert spoken language into another language's spoken output. It uses `speech_recognition` to capture and recognize speech, `googletrans` for translating text, and both `gtts` and `boto3` for text-to-speech functionality. This guide provides detailed steps for installing and running the application.

#### Prerequisites:
- Python 3.x installed on your system
- Internet connection (required for APIs like Google Translate and AWS Polly)

#### Installation Steps:

1. **Install Python**: Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Set up a Virtual Environment (recommended)**:
   Open a terminal and execute the following commands:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Python Packages**:
   You need to install `tkinter`, `speech_recognition`, `googletrans`, `gtts`, and `boto3`. Install these by running:
   ```bash
   pip install tk speech_recognition googletrans==4.0.0-rc1 gtts boto3
   ```

4. **AWS Credentials for Polly**:
   - Sign up or log into your AWS account.
   - Navigate to IAM and create a new user with programmatic access. Attach the `AmazonPollyFullAccess` policy.
   - Note the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.
   - Configure your credentials on your machine:
     ```bash
     aws configure
     ```
     Enter your access key, secret key, and default region when prompted.

5. **Running the Application**:
   - Ensure you're still in your virtual environment where all libraries are installed.
   - Navigate to the directory containing your script.
   - Run the script using Python:
     ```bash
     python <script_name>.py
     ```
   - The GUI will launch, and you can start using the application.

#### How to Use the Application:

1. **Start the application** as mentioned above.
2. **Select TTS System**: Choose from the dropdown which Text-to-Speech system to use.
3. **Select Input Language**: Choose the language you will speak.
4. **Select Output Language**: Choose the language into which you want the text translated.
5. **Choose Voice and Type**: Select the gender of the voice and whether to use a standard or neural voice.
6. **Start Translation**: Click the 'Start Translation' button and speak into your microphone. The application will translate and speak back the translated text in the chosen language.

#### Troubleshooting:

- **Microphone Issues**: Make sure your microphone is set as the default recording device and properly configured.
- **API Limitations**: Google Translate and AWS Polly have usage limits; ensure you're within limits or have a valid billing setup.
- **Library Versions**: If you encounter errors, check that you're using compatible versions of libraries, especially `googletrans` which is often updated.

This guide should help you set up and run the AI Voice Translator application smoothly. Ensure to follow each step carefully and check for software compatibility with your operating system.
