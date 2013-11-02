import sys
import os

DIR = ['Tech']
MD_DIR = [ d + '/' + 'md' for d in DIR ]

class publish :
    
    html_tpl_head = 'html_tpl/head.tpl'
    html_tpl_tail = 'html_tpl/tail.tpl'
    def __init__(self) :
        self.jobs = []
        for d in MD_DIR :
            self.getAllMdFiles(d)
   
    def md2Page(self, md_path, html_path) :
        transformedPage = os.popen('markdown_py %s' % (md_path,)).read()
        html_tpl_head_content = file(self.html_tpl_head).read()
        cnt = html_path.count('/')
        path_str = ''
        for i in range(cnt) : 
            path_str += '../'
        html_tpl_head_content = html_tpl_head_content.replace('', path_str)
        html_tpl_tail_content = file(self.html_tpl_tail).read()
        dump2page = file(html_path, 'w')
        dump2page.write(html_tpl_head_content)
        dump2page.write(transformedPage)
        dump2page.write(html_tpl_tail_content)
        dump2page.close()

    def getAllMdFiles(self, path) :
        if os.path.isdir(path) :
            dirlist = os.listdir(path)
            for item in dirlist :
                self.getAllMdFiles(path + '/' + item)
            return

        if path.find('.md') == len(path) - 3 :
            idx = path.rfind('/')
            filename = path[:len(path) - 3]
            html_path = path
            if idx > 0 : 
                filename = path[idx+1 : -3]
                html_path = path[:idx].replace('/md', '/html') 
                if os.path.exists(html_path) == False :
                    os.system('mkdir -p %s' % (html_path))
                html_path += '/' + filename + '.html'
            title = filename
            for line in file(path) :
                idx = line.find('#') 
                if idx < 0 : 
                    idx = line.find('<h1>')
                if idx >= 0 :
                    title = line[idx + 1:-1]
                    break

            self.jobs.append((title, path, html_path))

    def process(self) :
        cat2htmllist = {}
        for d in DIR :
            cat2htmllist[d] = []
        for title, md_path, html_path in self.jobs :
            print md_path
            print html_path
            self.md2Page(md_path, html_path)
            cat2htmllist[md_path[ : md_path.find('/')]].append((title, html_path))
        # generate outline for each category
        md_tpl = '* ###<a href="%s">%s</a>\n'
        for category in cat2htmllist :
            md_scripts = {}
            outline_md = file(category + '/index.md', 'w')
            outline_md.write('#%s\n' % (category,))
            for title, html_path in cat2htmllist[category] :
                child_category = html_path.split('/')[2]
                if child_category not in md_scripts :
                    md_scripts[child_category] = []
                md_scripts[child_category].append(md_tpl % (html_path[html_path.find('/') + 1:], title))
            
            for child_category in md_scripts :
                outline_md.write('##%s\n' % (child_category,))
                for md_script in md_scripts[child_category] :
                    outline_md.write(md_script)
            outline_md.close()
            self.md2Page(category + '/index.md' , category + '/index.html')

if __name__ == '__main__' :
    pb = publish()
    pb.process()

