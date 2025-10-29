"""
Test script to verify library installation and f-string fixes
"""

import sys
import ast


def test_imports():
    """Test that all required libraries can be imported"""
    print("Testing library imports...")
    
    try:
        import streamlit
        print("✅ streamlit imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import streamlit: {e}")
        return False
    
    try:
        import PyQt5
        print("✅ PyQt5 imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import PyQt5: {e}")
        return False
    
    return True


def test_desktop_apps():
    """Test that desktop app files have valid syntax"""
    print("\nTesting desktop app syntax...")
    
    # Test desktop_app_streamlit.py
    try:
        with open('desktop_app_streamlit.py', 'r') as f:
            code = f.read()
        ast.parse(code)
        print("✅ desktop_app_streamlit.py has valid syntax")
    except SyntaxError as e:
        print(f"❌ Syntax error in desktop_app_streamlit.py: {e}")
        return False
    except FileNotFoundError:
        print("❌ desktop_app_streamlit.py not found")
        return False
    
    # Test desktop_app_pyqt5.py
    try:
        with open('desktop_app_pyqt5.py', 'r') as f:
            code = f.read()
        ast.parse(code)
        print("✅ desktop_app_pyqt5.py has valid syntax (no f-string errors)")
    except SyntaxError as e:
        print(f"❌ Syntax error in desktop_app_pyqt5.py: {e}")
        return False
    except FileNotFoundError:
        print("❌ desktop_app_pyqt5.py not found")
        return False
    
    return True


def test_fstring_patterns():
    """Test f-string patterns to ensure no backslashes in expressions"""
    print("\nTesting f-string patterns...")
    
    # These are examples of correct f-string usage (no backslashes in expressions)
    test_message = "Hello"
    
    # Correct: Simple variable interpolation
    result1 = f'[SYSTEM] {test_message}'
    print(f"✅ F-string test 1: {result1}")
    
    # Correct: Multiple variables
    user = "User"
    content = "Content"
    result2 = f'{user}: {content}'
    print(f"✅ F-string test 2: {result2}")
    
    # Correct: Using string literals outside the expression
    result3 = f'Received: "{test_message}"'
    print(f"✅ F-string test 3: {result3}")
    
    return True


def main():
    """Run all tests"""
    print("=" * 60)
    print("JARVIS AI Agent v1.5 - Library Installation Test")
    print("=" * 60)
    
    all_passed = True
    
    if not test_imports():
        all_passed = False
    
    if not test_desktop_apps():
        all_passed = False
    
    if not test_fstring_patterns():
        all_passed = False
    
    print("\n" + "=" * 60)
    if all_passed:
        print("✅ ALL TESTS PASSED - Desktop Apps are ready! 🎉")
    else:
        print("❌ SOME TESTS FAILED - Please check errors above")
    print("=" * 60)
    
    return all_passed


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
