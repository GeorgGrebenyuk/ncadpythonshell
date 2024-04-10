﻿// Copyright (c) 2010 Joe Moorhouse

using ICSharpCode.AvalonEdit.Document;
using ICSharpCode.AvalonEdit.Highlighting;
using System;

namespace PythonConsoleControl
{
    /// <summary>
    /// Only colourize when text is input
    /// </summary>
    public class PythonConsoleHighlightingColorizer : HighlightingColorizer
    {
        private TextDocument document;

        /// <summary>
        /// Creates a new HighlightingColorizer instance.
        /// </summary>
        /// <param name="ruleSet">The root highlighting rule set.</param>
        public PythonConsoleHighlightingColorizer(IHighlightingDefinition ruleSet, TextDocument document)
            : base(ruleSet)
        {
            if (document == null)
                throw new ArgumentNullException("document");
            this.document = document;
        }

        /// <inheritdoc/>
        protected override void ColorizeLine(DocumentLine line)
        {
            IHighlighter highlighter = CurrentContext.TextView.Services.GetService(typeof(IHighlighter)) as IHighlighter;
            string lineString = document.GetText(line);
            if (highlighter != null)
            {
                if (lineString.Length < 3 || lineString.Substring(0, 3) == ">>>" || lineString.Substring(0, 3) == "...")
                {
                    HighlightedLine hl = highlighter.HighlightLine(line.LineNumber);
                    foreach (HighlightedSection section in hl.Sections)
                    {
                        ChangeLinePart(section.Offset, section.Offset + section.Length,
                                       visualLineElement => ApplyColorToElement(visualLineElement, section.Color));
                    }
                }
                else
                { // Could add foreground colour functionality here.
                }
            }
        }
    }
}