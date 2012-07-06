import sys;
import os;

class LineCount:
    def trim(self,docstring):
        if not docstring:
            return ''
        lines = docstring.expandtabs().splitlines()
        
        indent = sys.maxint
        for line in lines[1:]:
            stripped = line.lstrip()
            if stripped:
                indent = min(indent, len(line) - len(stripped))
        
        trimmed = [lines[0].strip()]
        if indent < sys.maxint:
            for line in lines[1:]:
                trimmed.append(line[indent:].rstrip())
        
        while trimmed and not trimmed[-1]:
            trimmed.pop()
        while trimmed and not trimmed[0]:
            trimmed.pop(0)
        
        return '\n'.join(trimmed)
    
    def FileLineCount(self,filename):
        (filepath,tempfilename) = os.path.split(filename);
        (shotname,extension) = os.path.splitext(tempfilename);
        if extension == '.txt' or extension == '.hol' : # file type 
            file = open(filename,'r');
            self.sourceFileCount += 1;
            allLines = file.readlines();
            file.close();
            
            lineCount    =0;
            commentCount = 0;
            blankCount   = 0;
            codeCount    = 0;
            for eachLine in allLines:
                if eachLine != " " :
                    eachLine = eachLine.replace(" ",""); #remove space
                    eachLine = self.trim(eachLine);      #remove tabIndent
                    if  eachLine.find('--') == 0 :  #LINECOMMENT 
                        commentCount += 1;
                    else :
                        if eachLine == "":
                            blankCount += 1;
                        else :
                            codeCount += 1;
                lineCount = lineCount + 1;
            self.all += lineCount;
            self.allComment += commentCount;
            self.allBlank += blankCount;
            self.allSource += codeCount;
            print filename;
            print '           Total      :',lineCount ;
            print '           Comment    :',commentCount;
            print '           Blank      :',blankCount;
            print '           Source     :',codeCount;
                    
    def CalulateCodeCount(self,filename):
        if os.path.isdir(filename) :
            if not filename.endswith('\\'):
                filename += '\\'; 
            for file in os.listdir(filename):
                if os.path.isdir(filename + file):
                    self.CalulateCodeCount(filename + file);
                else:
                    self.FileLineCount(filename + file);
        else:
            self.FileLineCount(filename);

    # Open File
    def __init__(self):
        self.all = 0;
        self.allComment =0;
        self.allBlank = 0;
        self.allSource = 0;
        self.sourceFileCount = 0;
        filename = raw_input('Enter file name: ');
        self.CalulateCodeCount(filename);
        if self.sourceFileCount == 0 :
            print 'No Code File';
            pass;
        print '\n';
        print '*****************  All Files  **********************';
        print '    Files      :',self.sourceFileCount;
        print '    Total      :',self.all;
        print '    Comment    :',self.allComment;
        print '    Blank      :',self.allBlank;
        print '    Source     :',self.allSource;
        print '****************************************************';

myLineCount = LineCount();
