using HostMgd.ApplicationServices;
using Teigha.Runtime;
using CADPythonShell.App;
using CADRuntime;
using Microsoft.Scripting;
using System.Windows;
using System.Windows.Interop;
using System.Windows.Threading;
using Application = HostMgd.ApplicationServices.Application;
using Exception = System.Exception;
using Forms = System.Windows.Forms;

namespace CADPythonShell.Command
{
    public class IronPythonConsoleCommand : ICadCommand
    {
        private static Guid ps_Attrs_id = Guid.Parse("{1f6e3f8d-c3ed-4e53-acc9-5113f6d615ca" +
            "}");
        private static HostMgd.Windows.PaletteSet ps_ConsolePalette;
        private static IronPythonConsole p_Console;

        /// <summary>
        /// Open a window to let the user enter python code.
        /// </summary>
        /// <returns></returns>
        public override void Execute()
        {
            Document doc = Application.DocumentManager.MdiActiveDocument;
            //load the application
            if (!CADPythonShellApplication.applicationLoaded)
            {
                CADPythonShellApplication.OnLoaded();
            }

            var gui = new IronPythonConsole();
            gui.consoleControl.WithConsoleHost((host) =>
            {
                // now that the console is created and initialized, the script scope should
                // be accessible...
                new ScriptExecutor(CADPythonShellApplication.GetConfig())
                    .SetupEnvironment(host.Engine, host.Console.ScriptScope);

                host.Console.ScriptScope.SetVariable("__window__", gui);

                // run the initscript
                var initScript = CADPythonShellApplication.GetInitScript();
                if (initScript != null)
                {
                    try
                    {
                        var scriptSource = host.Engine.CreateScriptSourceFromString(initScript, SourceCodeKind.Statements);
                        scriptSource.Execute(host.Console.ScriptScope);
                    }
                    catch (Exception ex)
                    {
                        Forms.MessageBox.Show(ex.ToString(), "Something went horribly wrong!");
                    }
                }
            });

            var dispatcher = Dispatcher.FromThread(Thread.CurrentThread);
            gui.consoleControl.WithConsoleHost((host) =>
            {
                host.Console.SetCommandDispatcher((command) =>
                {
                    if (command != null)
                    {
                        // Slightly involved form to enable keyboard interrupt to work.
                        var executing = true;
                        var operation = dispatcher.BeginInvoke(DispatcherPriority.Normal, command);
                        while (executing)
                        {
                            if (operation.Status != DispatcherOperationStatus.Completed)
                                operation.Wait(TimeSpan.FromSeconds(1));
                            if (operation.Status == DispatcherOperationStatus.Completed)
                                executing = false;
                        }
                    }
                });
                host.Editor.SetCompletionDispatcher((command) =>
                {
                    var executing = true;
                    var operation = dispatcher.BeginInvoke(DispatcherPriority.Normal, command);
                    while (executing)
                    {
                        if (operation.Status != DispatcherOperationStatus.Completed)
                            operation.Wait(TimeSpan.FromSeconds(1));
                        if (operation.Status == DispatcherOperationStatus.Completed)
                            executing = false;
                    }
                });
            });
            gui.WindowStartupLocation = WindowStartupLocation.CenterScreen;
            WindowInteropHelper helper = new WindowInteropHelper(gui);
            IntPtr hander = Application.MainWindow.Handle;
            helper.Owner = hander;
            gui.Show();
        }
        
        public static void RunConsole()
        {
            //if (ps_ConsolePalette == null)
            //{

            //    p_Console = gui;

            //    //use constructor with Guid so that we can save/load user data
            //    ps_ConsolePalette = new HostMgd.Windows.PaletteSet("nanoCAD Python Console", "nCADPythonShell", ps_Attrs_id);
            //    ps_ConsolePalette.MinimumSize = new System.Drawing.Size(520, 520);
            //    ps_ConsolePalette.Size = new System.Drawing.Size(520, 520);
            //    ps_ConsolePalette.Add("nanoCAD Python Console", p_Console);

            //    ps_ConsolePalette.Visible = true;
            //}
            //else
            //{
            //    if (!ps_ConsolePalette.Visible) ps_ConsolePalette.Visible = true;
            //    //ps_ConsolePalette.UpdateHandlers();
            //}

            


        }
    }
}