/***************************************************************
 * Name:      volunteersMain.h
 * Purpose:   Defines Application Frame
 * Author:    Jan Tulak (jan@tulak.me)
 * Created:   2015-07-21
 * Copyright: Jan Tulak ()
 * License:
 **************************************************************/

#ifndef VOLUNTEERSMAIN_H
#define VOLUNTEERSMAIN_H

//(*Headers(volunteersFrame)
#include <wx/notebook.h>
#include <wx/menu.h>
#include <wx/panel.h>
#include <wx/frame.h>
#include <wx/statusbr.h>
//*)

class volunteersFrame: public wxFrame
{
    public:

        volunteersFrame(wxWindow* parent,wxWindowID id = -1);
        virtual ~volunteersFrame();

    private:

        //(*Handlers(volunteersFrame)
        void OnQuit(wxCommandEvent& event);
        void OnAbout(wxCommandEvent& event);
        //*)

        //(*Identifiers(volunteersFrame)
        static const long ID_PANEL3;
        static const long ID_PANEL2;
        static const long ID_PANEL1;
        static const long ID_NOTEBOOK1;
        static const long idMenuQuit;
        static const long idMenuAbout;
        static const long ID_STATUSBAR1;
        //*)

        //(*Declarations(volunteersFrame)
        wxNotebook* Notebook1;
        wxPanel* Panel1;
        wxPanel* Panel3;
        wxStatusBar* StatusBar1;
        wxPanel* Panel2;
        //*)

        DECLARE_EVENT_TABLE()
};

#endif // VOLUNTEERSMAIN_H
