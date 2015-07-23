/***************************************************************
 * Name:      volunteersApp.cpp
 * Purpose:   Code for Application Class
 * Author:    Jan Tulak (jan@tulak.me)
 * Created:   2015-07-21
 * Copyright: Jan Tulak ()
 * License:
 **************************************************************/

#include "volunteersApp.h"

//(*AppHeaders
#include "volunteersMain.h"
#include <wx/image.h>
//*)

IMPLEMENT_APP(volunteersApp);

bool volunteersApp::OnInit()
{
    //(*AppInitialize
    bool wxsOK = true;
    wxInitAllImageHandlers();
    if ( wxsOK )
    {
    	volunteersFrame* Frame = new volunteersFrame(0);
    	Frame->Show();
    	SetTopWindow(Frame);
    }
    //*)
    return wxsOK;

}
