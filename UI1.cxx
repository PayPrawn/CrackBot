if (GetKeyState(VK_LBUTTON) < 0) {
{
POINT p;
if (GetCursorPos(&p))
{
cout<<"\nSCREEN\nx coord->";
cout<<p.x;
cout<<"\ny coord->";
cout<<p.y;
}
SetConsoleTitle("paint");
HWND hWnd;
hWnd = FindWindow(NULL, "paint");
if (ScreenToClient(hWnd, &p));
{
cout<<"\n\nWINDOW\nx coord->";
cout<<p.x;
cout<<"\ny coord->";
cout<<p.y;
}
int pwx;
int pwy;
pwx=p.x;
pwy=p.y;