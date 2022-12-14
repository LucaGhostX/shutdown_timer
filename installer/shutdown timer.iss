; Script generated by the Inno Script Studio Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{FOR SECURITY REASONS IT IS NOT AVAILABLE.}}
AppName=Shutdown Timer
AppVersion=2.3
AppVerName=Shutdown Timer 2.3
AppPublisher=LucaGhostX
AppPublisherURL=https://github.com/LucaGhostX/shutdown_timer
AppSupportURL=https://github.com/LucaGhostX/shutdown_timer
AppUpdatesURL=https://github.com/LucaGhostX/shutdown_timer
DefaultDirName={pf}\Shutdown Timer
DisableDirPage=yes
DefaultGroupName=Shutdown Timer Installer
DisableProgramGroupPage=yes
LicenseFile=C:\Users\lucag\Desktop\esercizi\shutdown nuovo\Nuova cartella\license.txt
OutputBaseFilename=ShutdownTimerInstaller_x64
Compression=zip
SolidCompression=yes
SetupIconFile=C:\Users\lucag\Desktop\esercizi\shutdown nuovo\Nuova cartella\installer.ico
VersionInfoCompany=LucaGhostX
VersionInfoProductName=Shutdown Timer Installer x64
VersionInfoProductVersion=2.3
VersionInfoVersion=0.0.2.3
AppCopyright=LucaGhostX

[Languages]
Name: "English"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 0,6.1

[Files]
Source: "..\dist\Shutdown Timer.exe"; DestDir: "{sd}\Shutdown Timer"; Flags: 64bit; Tasks: desktopicon quicklaunchicon; Check: IsWin64
Source: "..\GFSNeohellenic-Bold.ttf"; DestDir: "{fonts}"; Flags: ignoreversion uninsneveruninstall onlyifdoesntexist; FontInstall: """GFS Neohellenic"""

[Icons]
Name: "{group}\Shutdown Timer"; Filename: "{sd}\Shutdown Timer\Shutdown Timer.exe"
Name: "{commondesktop}\Shutdown Timer"; Filename: "{sd}\Shutdown Timer\Shutdown Timer.exe"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\Shutdown Timer"; Filename: "{sd}\Shutdown Timer\Shutdown Timer.exe"; Tasks: quicklaunchicon

[Run]
Filename: "{sd}\Shutdown Timer\Shutdown Timer.exe"; Description: "{cm:LaunchProgram,Shutdown Timer}"; Flags: nowait postinstall skipifsilent

