﻿// Copyright (c) 2010 Joe Moorhouse

using ICSharpCode.AvalonEdit;
using System.Windows.Media;

namespace PythonConsoleControl
{
    public class PythonConsolePad
    {
        private PythonTextEditor pythonTextEditor;
        private TextEditor textEditor;
        private PythonConsoleHost host;

        public PythonConsolePad()
        {
            textEditor = new TextEditor();
            pythonTextEditor = new PythonTextEditor(textEditor);
            host = new PythonConsoleHost(pythonTextEditor);
            host.Run();
            textEditor.FontFamily = new FontFamily("Consolas");
            textEditor.FontSize = 12;
        }

        public TextEditor Control
        {
            get { return textEditor; }
        }

        public PythonConsoleHost Host
        {
            get { return host; }
        }

        public PythonConsole Console
        {
            get { return host.Console; }
        }

        public void Dispose()
        {
            host.Dispose();
        }
    }
}