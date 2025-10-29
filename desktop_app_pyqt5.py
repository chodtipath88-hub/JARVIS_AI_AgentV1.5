"""
JARVIS AI Desktop Application - PyQt5 Version
A desktop interface for JARVIS AI Agent using PyQt5
"""

import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, 
    QHBoxLayout, QTextEdit, QPushButton, QLabel, QLineEdit
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class JarvisDesktopApp(QMainWindow):
    """Main application window for JARVIS AI Desktop App"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle('JARVIS AI Agent v1.5')
        self.setGeometry(100, 100, 800, 600)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Title label
        title_label = QLabel('JARVIS AI Agent v1.5')
        title_font = QFont('Arial', 16, QFont.Bold)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        # Chat display area
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setFont(QFont('Arial', 10))
        main_layout.addWidget(self.chat_display)
        
        # Input area layout
        input_layout = QHBoxLayout()
        
        # Input field
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText('Type your message here...')
        self.input_field.setFont(QFont('Arial', 10))
        self.input_field.returnPressed.connect(self.send_message)
        input_layout.addWidget(self.input_field)
        
        # Send button
        self.send_button = QPushButton('Send')
        self.send_button.setFont(QFont('Arial', 10))
        self.send_button.clicked.connect(self.send_message)
        input_layout.addWidget(self.send_button)
        
        main_layout.addLayout(input_layout)
        
        # Status bar
        self.statusBar().showMessage('Ready')
        
        # Add welcome message
        self.add_system_message('Welcome to JARVIS AI Agent v1.5!')
        self.add_system_message('Desktop Apps are ready to use! 🎉')
        
    def add_system_message(self, message):
        """Add a system message to the chat display"""
        formatted_message = f'[SYSTEM] {message}'
        self.chat_display.append(formatted_message)
        
    def add_user_message(self, message):
        """Add a user message to the chat display"""
        formatted_message = f'[USER] {message}'
        self.chat_display.append(formatted_message)
        
    def add_jarvis_response(self, message):
        """Add a JARVIS response to the chat display"""
        formatted_message = f'[JARVIS] {message}'
        self.chat_display.append(formatted_message)
        
    def send_message(self):
        """Handle sending a message"""
        user_input = self.input_field.text().strip()
        
        if not user_input:
            return
            
        # Add user message
        self.add_user_message(user_input)
        
        # Clear input field
        self.input_field.clear()
        
        # Process the message (placeholder for actual AI processing)
        self.process_message(user_input)
        
    def process_message(self, message):
        """Process user message and generate response"""
        # This is a placeholder. In a real implementation, 
        # this would connect to the JARVIS AI backend
        
        response = f'Received your message: "{message}"'
        self.add_jarvis_response(response)
        self.add_jarvis_response('AI processing is not yet connected. This is a UI demonstration.')


def main():
    """Main entry point for the application"""
    app = QApplication(sys.argv)
    window = JarvisDesktopApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
