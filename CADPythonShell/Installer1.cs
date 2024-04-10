//using Microsoft.Win32;
//using System;
//using System.Collections;
//using System.Collections.Generic;
//using System.ComponentModel;
//using System.Configuration.Install;
//using System.IO;
//using System.Linq;
//using System.Net;
//using System.Text;
//using System.Threading.Tasks;
//using System.Xml.Linq;

//namespace CADPythonShell
//{
//    [RunInstaller(true)]
//    public partial class Installer1 : System.Configuration.Install.Installer
//    {
//        public Installer1()
//        {
//            InitializeComponent();
//        }
//        private const string NPS_CFG_NAME = "NcPythonShell.cfg";
//        public override void Install(System.Collections.IDictionary stateSaver)
//        {
//            //string install_dir = "";
//            //using (RegistryKey key = Registry.LocalMachine.OpenSubKey("Software\\Wow6432Node\\Nanosoft_Dev\\nCAD Python Shell"))
//            //{
//            //    if (key != null)
//            //    {
//            //        Object o = key.GetValue("TARGETDIR");
//            //        if (o != null)
//            //        {
//            //            install_dir = o.ToString();
//            //        }
//            //    }
//            //}

//            //string nano_220_cfg = @$"C:\Users\{Environment.UserName}\AppData\Roaming\Nanosoft\nanoCAD x64 22.0\Config\nanoCAD.cfg";
//            //string nano_230_cfg = @$"C:\Users\{Environment.UserName}\AppData\Roaming\Nanosoft\nanoCAD x64 23.0\Config\nanoCAD.cfg";
//            //string nano_231_cfg = @$"C:\Users\{Environment.UserName}\AppData\Roaming\Nanosoft\nanoCAD x64 23.1\Config\nanoCAD.cfg";

//            ////EditFile(nano_220_cfg);
//            ////EditFile(nano_230_cfg);
//            ////EditFile(nano_231_cfg);

//            //void EditFile(string cfg_path)
//            //{
//            //    if (File.Exists(cfg_path))
//            //    {
//            //        StringBuilder cfg_new = new StringBuilder();
//            //        foreach (string cfg_str in File.ReadLines(cfg_path))
//            //        {
//            //            if (!cfg_str.Contains(NPS_CFG_NAME))
//            //            {
//            //                cfg_new.Append(cfg_str);
//            //            }
//            //        }
//            //        if (Directory.Exists(install_dir))
//            //        {
//            //            string cfg_nps_path = $"#include \"{install_dir}\\{NPS_CFG_NAME}\"";
//            //            cfg_new.Append(cfg_nps_path);
//            //        }
//            //        File.WriteAllText(cfg_path, cfg_new.ToString());
//            //    }
//            //}           
//        }
//        public override void Uninstall(System.Collections.IDictionary stateSaver)
//        {
//            //2 August 2019: Start, The next 3 lines were added in Take 10 in order prevent double loading of packages.
//            Microsoft.Win32.RegistryKey rkbase = null;
//            rkbase = Microsoft.Win32.RegistryKey.OpenBaseKey(Microsoft.Win32.RegistryHive.LocalMachine, Microsoft.Win32.RegistryView.Registry64);
//            rkbase.DeleteSubKeyTree("Software\\Wow6432Node\\Nanosoft_Dev\\nCAD Python Shell");
//        }
//    }
//}
