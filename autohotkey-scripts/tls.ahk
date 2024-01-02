::TrueLoveStory::{
CapsLock::
    KeyWait, CapsLock, T0.3
    if (ErrorLevel)
    {
        SetCapsLockState, % !GetKeyState("CapsLock", "T")
    }
    else
    {
        Send, {LAlt down}{LShift down}{LShift up}{LAlt up}
    }
return
}
