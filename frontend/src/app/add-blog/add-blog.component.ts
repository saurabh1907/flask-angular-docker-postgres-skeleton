import {Component, Input, OnInit} from "@angular/core";
import {BlogService} from "../service/blog.service";
import {Blog} from "../models/blog";

@Component({
  selector: "app-add-blog",
  templateUrl: "./add-blog.component.html",
  styleUrls: []
})
export class AddBlogComponent implements OnInit {
  @Input() public blog: Blog;
  @Input() public edit:boolean = false;

  public processing: boolean = false;
  public submitted: boolean = false;
  public success: boolean = false;
  public failure: boolean = false;

  constructor(private blogService: BlogService) {}

  ngOnInit() {
    if(this.blog == null)
      this.blog = new Blog();
  }

  public submit(): void {
    this.processing = this.submitted = true;

    console.log('submitting blog: ' + JSON.stringify(this.blog));

    if(this.edit == false){
      this.blogService.addBlog(this.blog).subscribe(
      // response => console.log('response on new post: ' + JSON.stringify(response))
      response => {
        // Handle each observable response
        console.log('result: ' + response);
        this.processing = false;
      },
      error => {
        this.processing = false;
        this.failure = true;
      },
      () => {
        this.processing = false;
        this.success = true;
      }
    );
    } else {
      this.blogService.editBlog(this.blog.id, this.blog).subscribe(
      // response => console.log('response on new post: ' + JSON.stringify(response))
      response => {
        // Handle each observable response
        console.log('result: ' + response);
        this.processing = false;
      },
      error => {
        this.processing = false;
        this.failure = true;
      },
      () => {
        this.processing = false;
        this.success = true;
      }
    );
    }
  }
}
