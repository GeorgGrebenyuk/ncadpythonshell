using Teigha.Runtime;
using CADPythonShell.Command;

namespace CADPythonShell.App
{
    public class IronPythonConsoleApp : IExtensionApplication
    {
        [CommandMethod("NPS_Run_NPS")]
        public void NPS_Run_NPS()
        {
            //new RelayCommand(new IronPythonConsoleCommand().Execute);
            new IronPythonConsoleCommand().Execute();
            //IronPythonConsoleCommand.RunConsole();
        }

        [CommandMethod("NPS_Configure_NPS")]
        public void NPS_Configure_NPS()
        {
            //new RelayCommand(new ConfigureCommand().Execute);
            new ConfigureCommand().Execute();
        }

        public void Initialize()
        {
            //throw new NotImplementedException();
        }

        public void Terminate()
        {
            //throw new NotImplementedException();
        }
    }
}