import {Component, OnInit, Input, Output, EventEmitter} from '@angular/core';
import { Router } from '@angular/router';
import {Blog} from '../models/blog';
import {BlogService} from "../service/blog.service";

@Component({
  selector: 'app-preview-blog',
  templateUrl: './preview-blog.component.html',
  styleUrls: []
})
export class PreviewBlogComponent implements OnInit {
  @Input() blog: Blog;

  @Output() deleteEvent = new EventEmitter();

  constructor(private router: Router, private blogService: BlogService) {}

  ngOnInit() {}

  public navigate(): void {
    this.router.navigateByUrl('/blogs/' + this.blog.id);
  }

  public deleteBlog() {
    this.blogService.deleteBlog(this.blog.id).subscribe(res => {
      console.log('Deleted Blog' + this.blog.id);
      this.deleteEvent.emit(this.blog);
    });
  }

}
