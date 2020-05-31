import { NgModule } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";
import {BlogListComponent} from "./blogs/blog-list.component";
import {AddBlogomponent} from "./blogs/add-blog.component";

const routes: Routes = [
  // { path: "", redirectTo: "", pathMatch: "full" },
  { path: "", component: BlogListComponent},
  { path: "**", redirectTo: "404", pathMatch: "full" },
  { path: 'add-blog', component: AddBlogomponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
