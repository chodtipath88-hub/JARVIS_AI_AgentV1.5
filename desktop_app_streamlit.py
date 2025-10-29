"""
JARVIS AI Desktop Application - Streamlit Version
A web-based interface for JARVIS AI Agent using Streamlit
"""

import streamlit as st


def init_session_state():
    """Initialize session state variables"""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
        # Add welcome messages
        st.session_state.messages.append({
            'role': 'system',
            'content': 'Welcome to JARVIS AI Agent v1.5!'
        })
        st.session_state.messages.append({
            'role': 'system',
            'content': 'Desktop Apps are ready to use! 🎉'
        })


def display_messages():
    """Display all messages in the chat"""
    for message in st.session_state.messages:
        role = message['role']
        content = message['content']
        
        if role == 'system':
            st.info(f'🤖 SYSTEM: {content}')
        elif role == 'user':
            st.write(f'👤 **USER:** {content}')
        elif role == 'assistant':
            st.success(f'🎯 **JARVIS:** {content}')


def process_user_input(user_input):
    """Process user input and generate response"""
    # Add user message
    st.session_state.messages.append({
        'role': 'user',
        'content': user_input
    })
    
    # Generate response (placeholder for actual AI processing)
    response = f'Received your message: "{user_input}"'
    st.session_state.messages.append({
        'role': 'assistant',
        'content': response
    })
    
    # Add info message
    st.session_state.messages.append({
        'role': 'assistant',
        'content': 'AI processing is not yet connected. This is a UI demonstration.'
    })


def main():
    """Main application function"""
    # Page configuration
    st.set_page_config(
        page_title='JARVIS AI Agent v1.5',
        page_icon='🤖',
        layout='wide'
    )
    
    # Initialize session state
    init_session_state()
    
    # Header
    st.title('🤖 JARVIS AI Agent v1.5')
    st.markdown('---')
    
    # Display chat messages
    st.subheader('Chat History')
    display_messages()
    
    st.markdown('---')
    
    # User input area
    st.subheader('Your Message')
    
    with st.form(key='message_form', clear_on_submit=True):
        user_input = st.text_input(
            'Type your message:',
            placeholder='Enter your message here...',
            label_visibility='collapsed'
        )
        submit_button = st.form_submit_button('Send')
        
        if submit_button and user_input.strip():
            process_user_input(user_input.strip())
            st.rerun()
    
    # Sidebar
    with st.sidebar:
        st.header('About')
        st.info('JARVIS AI Agent v1.5 - Streamlit Desktop App')
        st.markdown('---')
        
        st.header('Status')
        st.success('✅ Streamlit: Installed')
        st.success('✅ PyQt5: Installed')
        st.success('✅ Desktop Apps: Ready')
        
        st.markdown('---')
        
        if st.button('Clear Chat History'):
            st.session_state.messages = []
            init_session_state()
            st.rerun()


if __name__ == '__main__':
    main()
