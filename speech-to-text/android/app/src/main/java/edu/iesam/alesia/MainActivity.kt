package edu.iesam.alesia

import android.Manifest
import android.content.Intent
import android.content.pm.PackageManager
import android.os.Bundle
import android.speech.RecognitionListener
import android.speech.RecognizerIntent
import android.speech.SpeechRecognizer
import android.speech.tts.TextToSpeech
import android.text.Editable
import android.text.TextUtils
import android.util.Log
import android.widget.Toast
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat
import edu.iesam.alesia.databinding.ActivityMainBinding
import java.util.Locale

class MainActivity : AppCompatActivity(), TextToSpeech.OnInitListener {

    private lateinit var binding: ActivityMainBinding

    // Variables para SpeechRecognizer
    private var speechRecognizer: SpeechRecognizer? = null
    private var isListening = false
    private var accumulatedText = "" // Acumula el texto transcrito

    // Variables para TextToSpeech
    private var textToSpeech: TextToSpeech? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // Verificar y solicitar permisos
        checkAndRequestPermissions()

        // Inicializar SpeechRecognizer
        initializeSpeechRecognizer()

        // Inicializar TextToSpeech
        textToSpeech = TextToSpeech(this, this)

        // Botón para iniciar grabación y transcripción
        binding.startRecordingButton.setOnClickListener {
            if (checkPermissions()) {
                startSpeechRecognition()
            } else {
                Toast.makeText(this, "Se necesitan permisos para grabar audio", Toast.LENGTH_SHORT)
                    .show()
            }
        }

        // Botón para detener la grabación
        binding.stopRecordingButton.setOnClickListener {
            stopSpeechRecognition()
        }

        // Botón para convertir texto a audio
        binding.textToAudioButton.setOnClickListener {
            val text = binding.testText.text.toString()
            if (!TextUtils.isEmpty(text)) {
                speakText(text)
            } else {
                Toast.makeText(this, "Introduce un texto para convertir a audio", Toast.LENGTH_SHORT).show()
            }
        }

        // Botón para detener el audio
        binding.stopAudioButton.setOnClickListener {
            stopSpeaking()
        }
    }

    // **Inicialización de SpeechRecognizer**
    private fun initializeSpeechRecognizer() {
        speechRecognizer = SpeechRecognizer.createSpeechRecognizer(this)
        speechRecognizer?.setRecognitionListener(object : RecognitionListener {
            override fun onReadyForSpeech(params: Bundle?) {
                Log.d("@dev", "Ready to recognize speech")
                Toast.makeText(this@MainActivity, "Escuchando...", Toast.LENGTH_SHORT).show()
            }

            override fun onResults(results: Bundle?) {
                val matches = results?.getStringArrayList(SpeechRecognizer.RESULTS_RECOGNITION)
                val transcription = matches?.firstOrNull() ?: ""
                accumulatedText += "$transcription "
                binding.testText.text = Editable.Factory.getInstance().newEditable(accumulatedText.trim()) // Solución al problema de tipo
                Log.d("@dev", "Transcription: $transcription")

                // Reinicia automáticamente si seguimos escuchando
                if (isListening) {
                    startSpeechRecognition()
                }
            }

            override fun onPartialResults(partialResults: Bundle?) {
                val partial = partialResults?.getStringArrayList(SpeechRecognizer.RESULTS_RECOGNITION)
                val partialText = partial?.firstOrNull() ?: ""
                binding.testText.text = Editable.Factory.getInstance().newEditable(accumulatedText + partialText) // Solución al problema de tipo
            }

            override fun onError(error: Int) {
                Log.e("@dev", "Recognition error: $error")
                if (isListening) {
                    startSpeechRecognition()
                }
            }

            override fun onEndOfSpeech() {
                Log.d("@dev", "Speech ended")
                if (isListening) {
                    startSpeechRecognition()
                }
            }

            override fun onBeginningOfSpeech() {
                Log.d("@dev", "Speech started")
            }

            override fun onEvent(eventType: Int, params: Bundle?) {}
            override fun onBufferReceived(buffer: ByteArray?) {}
            override fun onRmsChanged(rmsdB: Float) {}
        })
    }

    private fun startSpeechRecognition() {
        val intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH).apply {
            putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
            putExtra(RecognizerIntent.EXTRA_LANGUAGE, Locale.getDefault())
            putExtra(RecognizerIntent.EXTRA_PARTIAL_RESULTS, true)
            putExtra(RecognizerIntent.EXTRA_MAX_RESULTS, 1)
        }

        if (!isListening) {
            accumulatedText = "" // Reinicia el texto acumulado
        }

        speechRecognizer?.startListening(intent)
        isListening = true
        Log.d("@dev", "Started speech recognition")
    }

    private fun stopSpeechRecognition() {
        isListening = false
        speechRecognizer?.stopListening()
        Log.d("@dev", "Stopped speech recognition")
        Toast.makeText(this, "Reconocimiento detenido", Toast.LENGTH_SHORT).show()
    }

    // **Funciones para Text-to-Speech**
    override fun onInit(status: Int) {
        if (status == TextToSpeech.SUCCESS) {
            val result = textToSpeech?.setLanguage(Locale.getDefault())
            if (result == TextToSpeech.LANG_MISSING_DATA || result == TextToSpeech.LANG_NOT_SUPPORTED) {
                Log.e("@dev", "El idioma seleccionado no es compatible o faltan datos")
                Toast.makeText(this, "El idioma seleccionado no está soportado", Toast.LENGTH_SHORT).show()
            } else {
                Log.d("@dev", "TextToSpeech inicializado correctamente")
            }
        } else {
            Log.e("@dev", "Error al inicializar TextToSpeech")
        }
    }

    private fun speakText(text: String) {
        textToSpeech?.speak(text, TextToSpeech.QUEUE_FLUSH, null, null)
        Log.d("@dev", "Reproduciendo texto: $text")
    }

    private fun stopSpeaking() {
        if (textToSpeech?.isSpeaking == true) {
            textToSpeech?.stop()
            Log.d("@dev", "Audio detenido")
        }
    }

    // **Permisos**
    private fun checkAndRequestPermissions() {
        val permissions = mutableListOf<String>()
        if (ContextCompat.checkSelfPermission(this, Manifest.permission.RECORD_AUDIO) != PackageManager.PERMISSION_GRANTED) {
            permissions.add(Manifest.permission.RECORD_AUDIO)
        }

        if (permissions.isNotEmpty()) {
            requestPermissionLauncher.launch(permissions.toTypedArray())
        }
    }

    private val requestPermissionLauncher =
        registerForActivityResult(ActivityResultContracts.RequestMultiplePermissions()) { permissions ->
            if (permissions.values.any { !it }) {
                Toast.makeText(this, "Permisos denegados", Toast.LENGTH_SHORT).show()
            } else {
                Toast.makeText(this, "Permisos concedidos", Toast.LENGTH_SHORT).show()
            }
        }

    private fun checkPermissions(): Boolean {
        return ContextCompat.checkSelfPermission(
            this,
            Manifest.permission.RECORD_AUDIO
        ) == PackageManager.PERMISSION_GRANTED
    }

    override fun onDestroy() {
        super.onDestroy()
        speechRecognizer?.destroy()
        speechRecognizer = null
        textToSpeech?.stop()
        textToSpeech?.shutdown()
    }
}